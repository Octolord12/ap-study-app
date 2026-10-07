-- AlterTable
ALTER TABLE "Topic" ADD COLUMN     "refresher" TEXT,
ADD COLUMN     "refresherReviewed" BOOLEAN NOT NULL DEFAULT false;
