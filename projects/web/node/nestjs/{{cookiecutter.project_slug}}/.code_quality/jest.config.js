export default {
  rootDir: "..",
  testEnvironment: "node",
  testMatch: ["<rootDir>/test/**/*.spec.ts"],
  extensionsToTreatAsEsm: [".ts"],
  moduleNameMapper: { "^(\\.{1,2}/.*)\\.js$": "$1" },
  transform: {
    "^.+\\.ts$": [
      "ts-jest",
      { useESM: true, tsconfig: "<rootDir>/.code_quality/tsconfig.test.json" },
    ],
  },
};
