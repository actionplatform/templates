import Constants from "expo-constants";
import { Link } from "expo-router";
import { StyleSheet, Text, View } from "react-native";

export default function About() {
  return (
    <View style={styles.container}>
      <Text accessibilityRole="header" style={styles.title}>
        About
      </Text>
      <Text style={styles.body}>
        Version {Constants.expoConfig?.version ?? "unknown"}
      </Text>
      <Link href="/" style={styles.link}>
        Back
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
    gap: 12,
  },
  title: { fontSize: 28, fontWeight: "700" },
  body: { fontSize: 16 },
  link: { fontSize: 16, color: "#2563eb" },
});
