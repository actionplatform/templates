module.exports = {
  presets: [
    ["@babel/preset-react", { runtime: "automatic" }],
    ["@babel/preset-env", { modules: false }],
  ],
  plugins: ["@babel/plugin-transform-class-properties"],
  env: {
    test: {
      presets: [
        ["@babel/preset-react", { runtime: "automatic" }],
        ["@babel/preset-env", { modules: "commonjs" }],
      ],
    },
  },
};
