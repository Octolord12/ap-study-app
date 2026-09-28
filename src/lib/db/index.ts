import { PrismaClient } from "@/generated/prisma/client";
import { PrismaNeon } from "@prisma/adapter-neon";

// Lazy singleton, not a top-level `new PrismaClient()`: Next.js evaluates
// imported modules during `next build`, and constructing eagerly would throw
// if DATABASE_URL isn't set yet (e.g. a fresh clone before `vercel env pull`).
// Also deliberately NOT a Proxy-wrapped client -- Auth.js's Prisma adapter
// inspects the client object directly, and a Proxy breaks those checks.
const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };

function createPrismaClient(): PrismaClient {
  const adapter = new PrismaNeon({ connectionString: process.env.DATABASE_URL! });
  return new PrismaClient({ adapter });
}

export function getDb(): PrismaClient {
  if (!globalForPrisma.prisma) {
    globalForPrisma.prisma = createPrismaClient();
  }
  return globalForPrisma.prisma;
}
