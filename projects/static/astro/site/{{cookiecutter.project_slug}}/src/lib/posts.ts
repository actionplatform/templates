export interface Post {
  id: string;
  body?: string;
  data: { title: string; date: Date; draft: boolean };
}

const WORDS_PER_MINUTE = 200;

export function published<T extends Post>(posts: T[]): T[] {
  return posts.filter((post) => !post.data.draft);
}

export function sortByDate<T extends Post>(posts: T[]): T[] {
  return [...posts].sort(
    (a, b) => b.data.date.getTime() - a.data.date.getTime()
  );
}

export function readingTime(text: string): number {
  const words = text.trim().split(/\s+/).filter(Boolean).length;

  return Math.max(1, Math.ceil(words / WORDS_PER_MINUTE));
}

export function formatDate(date: Date): string {
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    timeZone: "UTC",
  });
}
