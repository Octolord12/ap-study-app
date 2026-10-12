-- AlterEnum
-- This migration adds more than one value to an enum.
-- With PostgreSQL versions 11 and earlier, this is not possible
-- in a single migration. This can be worked around by creating
-- multiple migrations, each migration adding only one value to
-- the enum.


ALTER TYPE "FrqType" ADD VALUE 'RESULTS';
ALTER TYPE "FrqType" ADD VALUE 'RESULTS_GRAPH';
ALTER TYPE "FrqType" ADD VALUE 'INVESTIGATION';
ALTER TYPE "FrqType" ADD VALUE 'CONCEPT';
ALTER TYPE "FrqType" ADD VALUE 'MODEL';
ALTER TYPE "FrqType" ADD VALUE 'DATA';
