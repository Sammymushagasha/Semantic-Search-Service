import uuid
from datetime import datetime

from app.core.config import settings
from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, ForeignKey, String, Text, UniqueConstraint, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Gives all database models a shared base.
class Base(DeclarativeBase):
    pass


# Stores one ingested document and its basic details.
class Document(Base):
    __tablename__ = "documents"

    # Gives each document a unique ID.
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    # Stores a readable name and optional origin for the document.
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    # Records when the document was added.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    # Connects the document to its text chunks.
    chunks: Mapped[list["Chunk"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


# Stores a piece of document text and its optional search vector.
class Chunk(Base):
    __tablename__ = "chunks"
    __table_args__ = (
        UniqueConstraint("document_id", "chunk_index", name="uq_chunks_document_index"),
    )

    # Gives each chunk a unique ID.
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    # Links the chunk to its document and removes it when that document is deleted.
    document_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False,
    )
    # Keeps the chunk's position and searchable text.
    chunk_index: Mapped[int] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    # Reserves space for an embedding with the configured model's vector size.
    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(settings.search.embedding_dimension),
        nullable=True,
    )
    # Connects the chunk back to its document.
    document: Mapped[Document] = relationship(back_populates="chunks")
