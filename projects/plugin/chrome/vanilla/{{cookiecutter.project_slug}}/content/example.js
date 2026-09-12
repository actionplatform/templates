// Page-specific content script for https://example.com.
(function () {
  const { content } = self.{{ cookiecutter.package_name|upper }};

  content.watch(
    () => {
      const title = document.querySelector("h1")?.textContent?.trim();
      return title ? { source: "example", title } : null;
    },
    (event) => content.send(event)
  );
})();
