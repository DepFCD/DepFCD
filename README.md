# Dependency Facade: The Coupling and Conflicts between Android Framework and Its Customization

## Methodology
This directory contains the executable tools and scripts to analyze source code and history and implement experiments.

### The detection of Dependency facade

#### Entity and Dependency Extraction

- `enre_java.jar` - a static code analysis tool to produce dependencies graphs.
- input: source code path.
- command:
```java
java -jar <executable> <lang> <dir> <project-name>
```
The detailed information of the parameter and option of the command is:
```java
Usage: enre_java [-h] [-a=<aidl>] [-hd=<hidden>] [-d=<dir>]... <lang> <src>
                 <projectName>
      <lang>          The lanauge of project files: []
      <src>           The directory to be analyzed
      <projectName>   The analyzed project file name
  -a, --aidl=<aidl>   If the analyzed project is an Android project which
                        contains .aidl files, please provide the corresponding .
                        java files which have the same relative path with the
                        original file
  -d, --dir=<dir>     The additional directories to be analyzed
  -h, --help          display this help and exit
  -hd, --hidden=<hidden> The path of hiddenapi=flag.csv
```
- output: after analysis, ENRE-Java finally outputs the resolved entities and dependencies in JSON files in current directory，which contains corresponding dependency graph
  
#### Entity Ownership Identification
- jar or scripts
- input
- command
- output
  - `all_base_commits.csv` - the evolution history of all commits of the upstream AOSP frameworks/base
  - `<project name>-<version>`
    - blame_dict.csv - git blame detection result of current project selected merge node 
    - accompany_commits.csv - information of current project version's commit history
    - base_commits.csv - information of merge point which downstream project version merging upstream AOSP
    - old_base_commits.csv - commit history of current project version which belongs to upstream AOSP old version
    - only_accompany_commits.csv - commit history of current project version which belongs to downstream project
    - all_entities.csv - all entities and commits which contributed to specific entity information of files which contains intrusive modification of downstream project
    - final_ownership.csv - the entity ownership detection result below the 'File' level in the project
    - facade.json - the detection result of dependency facade of current project version

#### Intrusive Operation Identification
  This directory contains the data of different kinds of intrusive modification, following diagram shows the detail of each file.
- jar or scripts
- input
- command
- output:
  - `<project name>-<version>`
    - access_modify_entities.csv - The number of entity modifed by accessibility
    - final_modify_entities.csv - The number of entity modifed by 'final'
    - annotation_modify_entities.csv
    - add_import.json - The num of newly added statement of 'import'
    - inner_extensive_class_entities.csv - The num of newly added inner class in native class
    - parent_class_modify_entities.csv - The number of class modifed by parent class('inherit')
    - parent_interface_modify_entities.csv - The number of class modifed by parent interface('interface')
    - class_var_extensive_entities.csv - The number of newly added class field 
    - class_var_modify_entities.csv - The number of  modified class field 
    - method_var_modify_entities.csv -  The number of modified variable in method
    - param_modify_entities.csv  -  The number of method modified by parameters
    - return_type_modify_entities.csv - The number of method modified by return type
    - refactor_entities.csv - The number of refactoring entity(rename, extract and others)

### Restriction Level Labeling
- First, we get the current project version's non-SDK restriction level file by executing following command under the repo.

```
# Initialize the environment with the envsetup.sh script:
source build/envsetup.sh
# Choose which target to build with lunch
lunch <product_name-build_variant>
# output the non-SDK restriction level file
m out/soong/hiddenapi/hiddenapi.csv
```
- non-SDK restriction files (hiddenapi-flags.csv)

This directory contains data of non-SDK restriction files and the matching statistics, following diagram shows the details.

  - `matching.xlsx` - the matching statistics of non-SDK restriction files to dependency graph which is provided by ENRE
  - `hiddenapi-flags-<project name>-<version>.csv` - the 'hiddenapi-flags.csv' of downstream LineageOS 18.1 and 19.1, upstream AOSP 11 and 12. 

Then update the original dependency graph G by labeling non-SDK entities with their restriction levels through the command of `enre_java.jar`

## Set up
This directory contains the preliminary data to conduct following experiments and study our four research questions.

### Subject and Version Collection
This directory contains merge points which downstream project version merging upstream AOSP

### Merge Conflict Collection
This directory contains data of textual conflicts detection results of each project versions and details of manually selected conflict blocks.

- `<project name>-<version>-merge.csv` - the conflict details of current downstream project version which contains merge nodes, conflict files quantity, conflict java files quantity and conflict blocks LOC.

## Results
### RQ1: How do the downstream customizations rely on the upstream Android through interface-level dependencies?

- entity ownership distribution
  - `entity-ownership.xlsx` - the final collection of all project versions' entity ownership detection results
  - `<project name>-<version>`
    - final_ownership_count.csv - the number of each kind of entity combined with ownership detection result of current project version
- facade size measurements
  - `facade.xlsx` - the collection of all downstream project versions' dependency facade detection results
  - `<project name>-<version>`
    - `facade_base_info_count.csv` - The number of entity and dependency appearing in the dependency facade
    - `facade_file_filter.csv` - The number of each kind of entity appearing in the dependency facade which is counted in files
- interface-level dependencies (D->U)
  - `interface-level dep.xlsx` - the collection of all downstream project versions' interface-level dependencies facade detection results
  - `<project name>-<version>`
    - `interface_level_facade_d2u.csv` - The number of each kind of dependency appearing in the dependency facade(D->U)

### RQ2: How do the downstream customizations rely on the upstream Android through intrusion-level dependencies?

- intrusive operations
  - `intrusive-type.xlsx` - The collection of different kinds of intrusive modification's quantity for all project version
  - `<project name>-<version>`
    - `intrusive_count.xlsx` - The quantity of each kind of intrusive modification
    - `intrusive_file_count.csv` - The quantity of each kind of intrusive modification which is counted in files
- reverse dependencies
  - `<project name>-<version>`
    - `interface_level_facade_u2d.csv.csv` - The number of each kind of dependency appearing in the dependency facade(U->D)

### RQ3: How do the downstream customizations adapt to the dependency constraint imposed by the upstream Android?

- state transform and industrial modification
- non-SDK API usage

### RQ4: How do merge conflicts occur on the dependency facade between downstream customizations and the upstream Android?

- conflict blocks on the dependency facade
- `selected-conf-block.docx` - the selected conflict blocks details.

# Threats

First, our DepFCD employs the ENRE for entity and dependency extraction. It supports extracting possible dependencies caused by dynamic features, which other tools failed to identify. Second, the accuracy of Entity Ownership Identification and Intrusive Operation Identification of our DepFCD would impact the study of RQ1 and RQ2. To reduce threats, we combined the git blame command and advanced RefactoringMiner for an accurate analysis of commit history. git blame traces code modifications and RefactoringMiner identify refactoring operations involved in modifications. RefactoringMiner has been widely adopted in diverse work.

Our RQ3 employed the Restriction Level Labeling of DepFCD to assign the non-SDK restriction levels documented in “hiddenapi.csv” into the corresponding entities. To mitigate possible threats, we fetched and compiled the entire huge-scale
project repositories to generate accurate “hiddenapi.csv” files.

Our RQ4 conducted a manual study on the code conflicts on the dependency facade. To mitigate the possible subjectivity, the two authors of this work independently analyzed the conflict cases and reached consistent results. Moreover, we
reported the results on IndustrialX to its developers. They confirmed our observations on these cases, as discussed in Section V. We will analyze more conflict cases.

