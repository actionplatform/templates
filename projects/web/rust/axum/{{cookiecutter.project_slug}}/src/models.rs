//! The structs that cross the HTTP boundary.

use serde::{Deserialize, Serialize};

#[derive(Serialize)]
pub struct Health {
    pub status: &'static str,
    pub version: &'static str,
}

#[derive(Deserialize)]
pub struct ItemCreate {
    pub name: String,
}

#[derive(Clone, Debug, Serialize)]
pub struct Item {
    pub id: u64,
    pub name: String,
}
