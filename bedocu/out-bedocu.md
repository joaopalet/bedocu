## Bedocu

Bedocu is a Python package that allows users to create a project with several documents and get the summary for each of those documents. It also allows users to get a summary of a project which contains a summary of all the documents in that project. It can also return the filepath and summaries of all files in a project.

### Installation

```
pip install bedocu
```

### Usage

To create a project, use the `create_project()` function. This function takes a project name as an argument and returns a project object.

```
from bedocu import Bedocu

bedocu = Bedocu()
project = bedocu.create_project("My Project")
```

To add a document to a project, use the `add_document()` function. This function takes a document path as an argument and adds the document to the project.

```
project.add_document("/path/to/document.txt")
```

To get the summary of a document, use the `get_document_summary()` function. This function takes a document path as an argument and returns a summary of the document.

```
summary = project.get_document_summary("/path/to/document.txt")
```

To get the summary of a project, use the `get_project_summary()` function. This function takes a project object as an argument and returns a summary of the project.

```
summary = project.get_project_summary()
```

To get the filepath and summaries of all files in a project, use the `get_all_files()` function. This function takes a project object as an argument and returns a list of filepaths and summaries.

```
filepaths_and_summaries = project.get_all_files()
```
