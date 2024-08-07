-- User table
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL
);

-- DocumentType table
CREATE TABLE DocumentType (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    is_required BOOLEAN NOT NULL DEFAULT 0
);

-- Candidate table
CREATE TABLE Candidate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- CandidateDocument table
CREATE TABLE CandidateDocument (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    document_type_id INTEGER NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    verification_status TEXT NOT NULL,
    FOREIGN KEY (candidate_id) REFERENCES Candidate(id),
    FOREIGN KEY (document_type_id) REFERENCES DocumentType(id)
);

-- DocumentConfiguration table
CREATE TABLE DocumentConfiguration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_by INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES User(id)
);

-- ConfigurationDocumentType junction table
CREATE TABLE ConfigurationDocumentType (
    configuration_id INTEGER NOT NULL,
    document_type_id INTEGER NOT NULL,
    PRIMARY KEY (configuration_id, document_type_id),
    FOREIGN KEY (configuration_id) REFERENCES DocumentConfiguration(id),
    FOREIGN KEY (document_type_id) REFERENCES DocumentType(id)
);