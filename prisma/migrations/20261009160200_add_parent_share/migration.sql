-- CreateTable
CREATE TABLE "ParentShare" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "tokenHash" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expiresAt" TIMESTAMP(3) NOT NULL,
    "revokedAt" TIMESTAMP(3),
    "lastViewedAt" TIMESTAMP(3),

    CONSTRAINT "ParentShare_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "ParentShare_tokenHash_key" ON "ParentShare"("tokenHash");

-- CreateIndex
CREATE INDEX "ParentShare_userId_idx" ON "ParentShare"("userId");

-- AddForeignKey
ALTER TABLE "ParentShare" ADD CONSTRAINT "ParentShare_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

