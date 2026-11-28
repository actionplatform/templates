import { describe, expect, it } from "vitest";
import {
  formatDate,
  published,
  readingTime,
  sortByDate,
  type Post,
} from "../src/lib/posts";

const post = (id: string, date: string, draft = false): Post => ({
  id,
  data: { title: id, date: new Date(date), draft },
});

describe("sortByDate", () => {
  it("puts the newest post first", () => {
    const posts = [
      post("a", "2025-01-01"),
      post("c", "2025-03-01"),
      post("b", "2025-02-01"),
    ];

    expect(sortByDate(posts).map((p) => p.id)).toEqual(["c", "b", "a"]);
  });

  it("does not mutate its input", () => {
    const posts = [post("a", "2025-01-01"), post("b", "2025-02-01")];

    sortByDate(posts);

    expect(posts.map((p) => p.id)).toEqual(["a", "b"]);
  });
});

describe("published", () => {
  it("drops drafts", () => {
    const posts = [post("a", "2025-01-01"), post("b", "2025-02-01", true)];

    expect(published(posts).map((p) => p.id)).toEqual(["a"]);
  });
});

describe("readingTime", () => {
  it("is at least one minute", () => {
    expect(readingTime("")).toBe(1);
    expect(readingTime("one two three")).toBe(1);
  });

  it("rounds up at 200 words per minute", () => {
    expect(readingTime("word ".repeat(200))).toBe(1);
    expect(readingTime("word ".repeat(201))).toBe(2);
    expect(readingTime("word ".repeat(1000))).toBe(5);
  });
});

describe("formatDate", () => {
  it("formats in UTC", () => {
    expect(formatDate(new Date("2025-01-15T00:00:00Z"))).toBe(
      "January 15, 2025"
    );
  });
});
