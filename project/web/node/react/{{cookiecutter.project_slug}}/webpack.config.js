const path = require("path");
const Dotenv = require("dotenv-webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = (env) => {
  const mode = env.mode || "production";
  const isProduction = mode === "production";

  return {
    mode,
    entry: "./src/index.js",
    output: {
      publicPath: "/",
      path: path.resolve(__dirname, "build"),
      filename: isProduction ? "[name].[contenthash:8].js" : "[name].js",
      chunkFilename: isProduction ? "[name].[contenthash:8].chunk.js" : "[name].chunk.js",
      clean: true,
    },
    devtool: isProduction ? false : "eval-source-map",
    optimization: {
      minimize: isProduction,
      minimizer: [new TerserPlugin({ terserOptions: { compress: { drop_console: true } } })],
      splitChunks: {
        chunks: "all",
        cacheGroups: {
          react: {
            test: /[\\/]node_modules[\\/](react|react-dom|scheduler|react-router|react-router-dom)[\\/]/,
            name: "vendor-react",
            priority: 40,
          },
          vendor: { test: /[\\/]node_modules[\\/]/, name: "vendors", priority: 10 },
        },
      },
    },
    module: {
      rules: [
        {
          test: /\.module\.(css|scss)$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : "style-loader",
            { loader: "css-loader", options: { modules: { localIdentName: "[name]__[local]__[hash:base64:5]" } } },
            "sass-loader",
          ],
        },
        {
          test: /\.(css|scss)$/,
          exclude: /\.module\.(css|scss)$/,
          use: [isProduction ? MiniCssExtractPlugin.loader : "style-loader", "css-loader", "sass-loader"],
        },
        {
          test: /\.(png|jpe?g|gif|svg|ico)$/i,
          type: "asset",
          generator: { filename: "images/[name].[hash][ext]" },
        },
        { test: /\.(js|jsx)$/, exclude: /node_modules/, use: "babel-loader" },
      ],
    },
    resolve: {
      alias: {
        components: path.resolve(__dirname, "src/components"),
        hooks: path.resolve(__dirname, "src/hooks"),
        utils: path.resolve(__dirname, "src/utils"),
        constants: path.resolve(__dirname, "src/constants"),
        stores: path.resolve(__dirname, "src/stores"),
        lib: path.resolve(__dirname, "src/lib"),
      },
      extensions: [".js", ".jsx", ".css", ".scss"],
    },
    plugins: [
      new HtmlWebpackPlugin({ template: "./public/index.html" }),
      new Dotenv({ systemvars: true }),
      ...(isProduction
        ? [new MiniCssExtractPlugin({ filename: "[name].[contenthash:8].css", chunkFilename: "[name].[contenthash:8].chunk.css" })]
        : []),
    ],
    devServer: {
      static: path.resolve(__dirname, "public"),
      port: 3000,
      historyApiFallback: true,
      proxy: [{ context: ["/api"], target: "http://127.0.0.1:8000", changeOrigin: true }],
    },
  };
};
