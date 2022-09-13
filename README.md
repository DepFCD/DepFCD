# Dependency Facade: The Coupling and Conflicts between Android Framework and Its Customization
This project contains the tool, data, and scripts of our ICSE 2023 under-reviewing work —— `Dependency Facade: The Coupling and Conflicts between Android Framework and Its Customization`. The directory is conducted as follows.
Please note that due to paper page limit, we attach Section `Threats to Validity` <here>. We opened all of the collected data of the investigated subjects. As for the industrial (IndustrialX) subject, because of the confidential issue and file size limit of GitHub, we only upload key research data and scripts to this repository. 

The whole directory goes like the following:
```
│  README.md
│  
├─Data
│  ├─Methodology
│  │  ├─ENtity_and_Dependency_Extraction
│  │  ├─Entity_Ownership_Identification      
│  │  ├─Intrusive_Operation_Identification   
│  │  └─Restriction_Level_Labeling 
│  ├─Results
│  │  ├─RQ1    
│  │  ├─RQ2
│  │  ├─RQ3
│  │  └─RQ4
│  │          
│  └─Setup
│      ├─Merge_conflict_collection
│      │  ├─aospa
│      │  ├─calyx
│      │  ├─lineage
│      │  └─omnirom
│      │          
│      └─Subject_and_version_collection
│          ├─aospa
│          ├─calyx
│          ├─lineage
│          └─omnirom
│                  
├─Method
│  │  dep_facade.exe
│  │  enre_java.jar
│  │  
│  └─ref_tool
│              
└─Scripts
    ├─RQ_scripts
    └─setup_scripts
```

## Method

### Entity and Dependency Extraction

- `enre_java.jar` - a static code analysis tool to produce dependencies graphs.

- input: source code path， hidden flag file path

- command:

```powershell
java -jar enre_java.jar java <local_path_to_repo\LineageOS\base\services\core\java\com\android\server> lineage -hd hiddenapi-flags-lineage18.csv
```

### Entity Ownership  and Intrusive Operation Identification

- `dep_facade.exe` - a dependency facade analysis tool to detect entities' ownership and intrusive operation in dependencies  graph and in this tool we encapsulate the tool `RefactoringMiner`
  - `ref_tool\lib\RefactoringMiner-2.2.0.jar` - the refactoring infomation detection tool, there are some `jar` required for the tool in the `ref_tool\lib` directory
  - `ref_tool\bin\RefactoringMiner` - a script that executes the tool `Refactoring Miner-2.2.0.jar` to generate refactoring information
- input: source code path, source dependencies graph json file path
- command:

```powershell
dep_facade.exe -cc <local_path_to_downstream_repo\LineageOS\base> -ca <local_path_to_upstream_repo\android\base> -c <path_to_downstream_dependency_graph, i.e. D:\LineageOS\lineage.json> -a <path_to_upstream_dependency_graph, i.e. D:\android\android.json> -ref ref_tool\bin\RefactoringMiner -o <output_path>
```

During the detecting process， we need to acquire all commits history of AOSP all versions， which is time-consuming. To save some time， you can put the `all_base_commits.csv` which is provided by Section `data\Methodology\The detection of Dependency facade \Entity Ownership Identification`.

The WARNING which is related to `log4j` during the executing process is ignorable. 

## Scripts

### Set up
We use the following scripts to get the merge points and conflicts, most of them are from https://zenodo.org/record/6272071#.Yxg_OWhBw_E.
To execute them, users need to satisfy the following steps.
1. Clone corresponding customized Android Frameworks into directory platforms.
2. Retrieve the commit history of customized Android Frameworks and store it in directory history.
3. Run Python scripts to acquire merge and conflict information.
Every Python script contains the specification of the intention at the beginning of the script.
However, the path specified in the script should be replaced with the local path as I am using the absolute path.
We also provide specific scripts we use in this directory.
1. After cloning the repo,  users also need to create `/<project>` folder which contains `branch_all.txt` and `/branches` empty folder, the `branch_all.txt` contains all branches of versions.
2. Then, run `andro_base_branch_commit_hist.py` to retrieve commit history.
3. After that, run `merge_extract.py` to acquire all merge points.
4. Finally, run `merge_conf_detect.py` to detect the merge conflicts and `merge_conf_ast.py` to get the details of conflict blocks.

## Data

### Methodology

This directory contains the executable tools and scripts to analyze source code and history and implement experiments.

#### The detection of Dependency facade

##### Entity and Dependency Extraction

- `enre_java.jar` - a static code analysis tool to produce dependencies graphs.
- input: source code path.
- command:
```java
java -jar <executable> <lang> <dir> <project-name> -hd <path-to-hiddenapi-flags.csv>
```
- output: after analysis, ENRE-Java finally outputs the resolved entities and dependencies in JSON files in the current directory， which contains the corresponding dependency graph
  
##### Entity Ownership Identification
This directory contains the data of commits history, ownership, and dependency facade information generated by running the tool `dep_facade.exe`, following diagram shows the detail of each file.

- `all_base_commits.csv` - the evolution history of all commits of the upstream AOSP frameworks/base
- `<project name>-<version>`
	- blame_dict.csv - git blame detection result of the current project selected merge node 
	- accompany_commits.csv - information of current project version's commit history
	- base_commits.csv - information of merge point which downstream project version merging upstream AOSP
	- old_base_commits.csv - commit history of current project version which belongs to upstream AOSP old version
	- only_accompany_commits.csv - commit history of current project version which belongs to downstream project
	- all_entities.csv - all entities and commits that contributed to specific entity information of files that contains an intrusive modification of the downstream project
	- final_ownership.csv - the entity ownership detection result below the 'File' level in the project
	- facade.json - the detection result of dependency facade of current project version


##### Intrusive Operation Identification
This directory contains the data of different kinds of intrusive modification generate by running the tool `dep_facade.exe`,  following diagram shows the detail of each file.

- `<project name>-<version>`
	- access_modify_entities.csv - The number of entities modified by accessibility
	- final_modify_entities.csv - The number of entities modified by 'final'
	- annotation_modify_entities.csv
	- add_import.json - The num of newly-added statements of 'import'
	- inner_extensive_class_entities.csv - The num of newly added inner classes in the native class
	- parent_class_modify_entities.csv - The number of classes modified by the parent class('inherit')
	- parent_interface_modify_entities.csv - The number of classes modified by the parent interface('interface')
	- class_var_extensive_entities.csv - The number of newly added class field 
	- class_var_modify_entities.csv - The number of  modified class field 
	- method_var_modify_entities.csv -  The number of modified variables in the method
	- param_modify_entities.csv  -  The number of methods modified by parameters
	- return_type_modify_entities.csv - The number of methods modified by return type
	- refactor_entities.csv - The number of refactoring entities (rename, extract, and others)

#### Restriction Level Labeling
- First, we get the current project version's non-SDK restriction level file by executing the following command under the repo.

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

- `matching.xlsx` - the matching statistics of non-SDK restriction files to the dependency graph which is provided by ENRE
- `hiddenapi-flags-<project name>-<version>.csv` - the 'hiddenapi-flags.csv' of downstream LineageOS 18.1 and 19.1, upstream AOSP 11 and 12. 

Then update the original dependency graph G by labeling non-SDK entities with their restriction levels through the command of `enre_java.jar`

### Set up
This directory contains the preliminary data to conduct the following experiments and study our four research questions.

#### Subject and Version Collection
This directory contains merge points in which downstream project versions merge upstream AOSP

- `<project name>-<version>-merge.csv` - the merge points of the current downstream project version which contains merge commit, both upstream and downstream's parent commits and branches.

#### Merge Conflict Collection
This directory contains data on textual conflict detection results of each project version and details of manually selected conflict blocks.

- `<project name>-<version>-merge.csv` - the conflict details of the current downstream project version which contains merge nodes, conflict files quantity, conflict java files quantity, and conflict blocks LOC.

### Results
#### RQ1: How do the downstream customizations rely on the upstream Android through interface-level dependencies?

- entity ownership distribution
  - `entity-ownership.xlsx` - the final collection of all project versions' entity ownership detection results
  - `<project name>-<version>`
    - final_ownership_count.csv - the number of each kind of entity combined with the ownership detection result of the current project version
- facade size measurements
  - `facade.xlsx` - the collection of all downstream project versions' dependency facade detection results
  - `<project name>-<version>`
    - `facade_base_info_count.csv` - The number of entities and dependencies appearing in the dependency facade
    - `facade_relation_info_count.csv` - The number of each kind of dependency appearing in the dependency facade
    - `facade_file_filter.csv` - The number of each kind of entity appearing in the dependency facade which is counted in files
- interface-level dependencies (D->U)
  - `interface-level dep.xlsx` - the collection of all downstream project versions' interface-level dependencies facade detection results
  - `<project name>-<version>`
    - `interface_level_facade_d2u.csv` - The number of each kind of dependency appearing in the dependency facade(D->U)

#### RQ2: How do the downstream customizations rely on the upstream Android through intrusion-level dependencies?

- intrusive operations
  - `intrusive-type.xlsx` - The collection of different kinds of intrusive modifications quantity for all project version
  - `<project name>-<version>`
    - `intrusive_count.csv` - The quantity of each kind of intrusive modification
    - `intrusive_file_count.csv` - The quantity of each kind of intrusive modification which is counted in files
- reverse dependencies
  - `<project name>-<version>`
    - `interface_level_facade_u2d.csv` - The number of each kind of dependency appearing in the dependency facade(U->D)

#### RQ3: How do the downstream customizations adapt to the dependency constraint imposed by the upstream Android?

- state transformation and industrial modification
- non-SDK API usage

#### RQ4: How do merge conflicts occur on the dependency facade between downstream customizations and the upstream Android?

- `selected-conf-block.docx` - the selected conflict blocks details.

# Threats

First, our DepFCD employs the ENRE for entity and dependency extraction. It supports extracting possible dependencies caused by dynamic features, which other tools failed to identify. Second, the accuracy of Entity Ownership Identification and Intrusive Operation Identification of our DepFCD would impact the study of RQ1 and RQ2. To reduce threats, we combined the git blame command and advanced RefactoringMiner for an accurate analysis of commit history. git blame traces code modifications and RefactoringMiner identifies refactoring operations involved in modifications. RefactoringMiner has been widely adopted in diverse work.

Our RQ3 employed the Restriction Level Labeling of DepFCD to assign the non-SDK restriction levels documented in “hiddenapi.csv” into the corresponding entities. To mitigate possible threats, we fetched and compiled the entire huge-scale
project repositories to generate accurate “hiddenapi.csv” files.

Our RQ4 conducted a manual study on the code conflicts on the dependency facade. To mitigate the possible subjectivity, the two authors of this work independently analyzed the conflict cases and reached consistent results. Moreover, we
reported the results on IndustrialX to its developers. They confirmed our observations on these cases, as discussed in Section V. We will analyze more conflict cases.

