-- CreateEnum
CREATE TYPE "FrqType" AS ENUM ('FRQ', 'SAQ', 'DBQ', 'LEQ');

-- AlterTable
ALTER TABLE "FRQPrompt" ADD COLUMN     "type" "FrqType" NOT NULL DEFAULT 'FRQ';
