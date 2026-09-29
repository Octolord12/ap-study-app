/*
  Warnings:

  - Added the required column `frqPromptIds` to the `ExamAttempt` table without a default value. This is not possible if the table is not empty.
  - Added the required column `questionIds` to the `ExamAttempt` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "ExamAttempt" ADD COLUMN     "frqPromptIds" JSONB NOT NULL,
ADD COLUMN     "questionIds" JSONB NOT NULL,
ALTER COLUMN "sectionScores" DROP NOT NULL,
ALTER COLUMN "estimatedScore" DROP NOT NULL;
