#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    {{ cookiecutter.package_name }}_lib::run()
}
