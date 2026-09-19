use {{ cookiecutter.package_name }}::hello;

#[test]
fn greets_from_outside_the_crate() {
    assert_eq!(hello("ana"), "hello, ana");
}
