use std::collections::BTreeMap;
use std::fmt;
use std::sync::Mutex;

use crate::models::Item;

const MAX_NAME: usize = 40;

#[derive(Debug, PartialEq)]
pub enum Error {
    Invalid(String),
    NotFound(String),
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Error::Invalid(reason) => write!(f, "invalid: {reason}"),
            Error::NotFound(id) => write!(f, "not found: item {id}"),
        }
    }
}

#[derive(Default)]
struct Store {
    rows: BTreeMap<u64, Item>,
    last_id: u64,
}

/// Keeps items in memory, standing in for a database or an external API. Replace the storage; keep the methods.
#[derive(Default)]
pub struct Items {
    store: Mutex<Store>,
}

impl Items {
    pub fn list(&self) -> Vec<Item> {
        self.store.lock().unwrap().rows.values().cloned().collect()
    }

    pub fn get(&self, id: u64) -> Result<Item, Error> {
        self.store
            .lock()
            .unwrap()
            .rows
            .get(&id)
            .cloned()
            .ok_or_else(|| Error::NotFound(id.to_string()))
    }

    pub fn create(&self, name: &str) -> Result<Item, Error> {
        let name = name.trim();

        if name.is_empty() {
            return Err(Error::Invalid("name is required".into()));
        }

        if name.chars().count() > MAX_NAME {
            return Err(Error::Invalid(format!(
                "name is longer than {MAX_NAME} characters"
            )));
        }

        let mut store = self.store.lock().unwrap();
        store.last_id += 1;
        let item = Item {
            id: store.last_id,
            name: name.to_string(),
        };
        store.rows.insert(item.id, item.clone());

        Ok(item)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn create_trims_and_numbers() {
        let items = Items::default();

        let first = items.create("  first  ").unwrap();
        let second = items.create("second").unwrap();

        assert_eq!((first.id, first.name.as_str()), (1, "first"));
        assert_eq!(second.id, 2);
    }

    #[test]
    fn create_rejects_empty_name() {
        let err = Items::default().create("   ").unwrap_err();

        assert_eq!(err, Error::Invalid("name is required".into()));
    }

    #[test]
    fn create_rejects_long_name() {
        let err = Items::default().create(&"a".repeat(41)).unwrap_err();

        assert!(matches!(err, Error::Invalid(_)));
    }

    #[test]
    fn get_unknown_is_not_found() {
        let err = Items::default().get(9).unwrap_err();

        assert_eq!(err, Error::NotFound("9".into()));
    }

    #[test]
    fn list_returns_created_items() {
        let items = Items::default();
        items.create("a").unwrap();
        items.create("b").unwrap();

        assert_eq!(items.list().len(), 2);
    }
}
