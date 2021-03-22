# Microtask 3

- What is the meaning of the JSON attribute author_id?
  - Event actor ID from SortingHat profile
  - Used to identify an author. 
  - These are used to group into a single author_uuid.
- What is the meaning of the JSON attribute author_org_name?
  - Organization name to which the author is affiliated to
  - Can be affiliated to multiple organisation separately.
- What is the meaning of the JSON attribute author_uuid?
  - Author profile unique identifier. It is used for counting authors and cross-referencing data among the data sources. 
- What is the meaning of the JSON attribute author_domain?
  - Domain associated to the author in SortingHat profile.
- What is the meaning of the JSON attribute uuid?
  - uuid is Unique Identifier, which keeps track of how many unique profiles are stored.
- What is the meaning of the JSON attribute utc_commit?
  - Commit date in UTC.
  - Related to commits in git version control system.
- What is the meaning of the JSON attribute origin?
  - The original source from which the data is retreived from.

References:
- https://github.com/chaoss/grimoirelab-elk/blob/master/README.md
