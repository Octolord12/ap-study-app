// Vercel writes DATABASE_URL into .env.local (via `vercel env pull`), not .env,
// so we load that explicitly — dotenv's default config() only reads .env.
import { config } from "dotenv";
import { defineConfig } from "prisma/config";

config({ path: ".env.local" });

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: process.env["DATABASE_URL"],
  },
});
