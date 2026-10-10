-- CreateTable
CREATE TABLE "ClassBan" (
    "classId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "bannedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ClassBan_pkey" PRIMARY KEY ("classId","userId")
);

-- AddForeignKey
ALTER TABLE "ClassBan" ADD CONSTRAINT "ClassBan_classId_fkey" FOREIGN KEY ("classId") REFERENCES "Class"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ClassBan" ADD CONSTRAINT "ClassBan_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

