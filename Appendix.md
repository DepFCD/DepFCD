# Appendix 

This appendix supplements the definition, the missed data and description of paper.

## Table 1 The range of tags of upstream version

This table specify the merge points of upstream Android tags in corresponding versions(branches).

<table>
    <tr>
        <td>Project</td>
        <td colspan="4">Downstream Version</td>
        <td colspan="4">Upstream(AOSP) Version</td>
        <td colspan="2">Merge Commits</td>
    </tr>
    <tr>
        <td></td>
        <td>Version</td>
        <td>#File</td>
        <td>#Loc</td>
        <td>#Commit</td>
        <td>Version</td>
        <td>#File</td>
        <td>#Loc</td>
        <td>#Commit</td>
        <td>#MerCmt</td>
        <td>#CflCmt</td>
    </tr>
    <tr>
        <td rowspan="3">AOSPA</td>
        <td>Sapphire</td>
        <td>27,539</td>
        <td>4,575,525</td>
        <td>674,953</td>
        <td>android12-gsi(898ad0236f7)</td>
        <td>27,308</td>
        <td>4,526,922</td>
        <td>611,807</td>
        <td>46</td>
        <td>37</td>
    </tr>
    <tr>
        <td>Ruby</td>
        <td>26,497</td>
        <td>4,165,240</td>
        <td>501,248</td>
        <td>android11-qpr1-d-release(ca05b4c5f77)</td>
        <td>26,429</td>
        <td>4,147,331</td>
        <td>650,983</td>
        <td>64</td>
        <td>47</td>
    </tr>
    <tr>
        <td>Quartz</td>
        <td>19,939</td>
        <td>3,188,444</td>
        <td>420,479</td>
        <td>android11-d2-release(823838e9efc)</td>
        <td>19,913</td>
        <td>3,175,862</td>
        <td>498,028</td>
        <td>99</td>
        <td>52</td>
    </tr>
    <tr>
        <td rowspan="2">CalyxOS</td>
        <td>android12</td>
        <td>27,384</td>
        <td>4,530,132</td>
        <td>651,640</td>
        <td>android12-qpr1-d-release(android-12.0.0_r29)</td>
        <td>27,308</td>
        <td>4,526,923</td>
        <td>649,754</td>
        <td>5</td>
        <td>2</td>
    </tr>
    <tr>
        <td>android11</td>
        <td>26,699</td>
        <td>4,169,261</td>
        <td>482,229</td>
        <td>android11-qpr3-release(android-11.0.0_r46)</td>
        <td>26,463</td>
        <td>4,155,454</td>
        <td>497,949</td>
        <td>10</td>
        <td>1</td>
    </tr>
    <tr>
        <td rowspan="4">LineageOS</td>
        <td>LineageOS-19.1</td>
        <td>27,685</td>
        <td>4,576,171</td>
        <td>663,065</td>
        <td>android12-qpr3-s1-release(android-12.1.0_r7)</td>
        <td>27,469</td>
        <td>4,558,550</td>
        <td>659,793</td>
        <td>3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>LineageOS-18.1</td>
        <td>26,713</td>
        <td>4,190,090</td>
        <td>499,427</td>
        <td>android11-gsi(android-11.0.0_r46)</td>
        <td>22,534</td>
        <td>3,669,603</td>
        <td>505,590</td>
        <td>17</td>
        <td>8</td>
    </tr>
    <tr>
        <td>LineageOS-17.1</td>
        <td>22,951</td>
        <td>3,711,094</td>
        <td>426,543</td>
        <td>android-s-beta-4(android-10.0.0_r41)</td>
        <td>22,455</td>
        <td>3,652,993</td>
        <td>571,185</td>
        <td>28</td>
        <td>12</td>
    </tr>
    <tr>
        <td>LineageOS-16.0</td>
        <td>2,0293</td>
        <td>3,212,780</td>
        <td>371,425</td>
        <td>android-s-beta-4(android-9.0.0_r61)</td>
        <td>19,871</td>
        <td>3,171,811</td>
        <td>369,065</td>
        <td>50</td>
        <td>12</td>
    </tr>
    <tr>
        <td rowspan="4">OmniROM</td>
        <td>android-12.0</td>
        <td>27,351</td>
        <td>4,530,005</td>
        <td>650,684</td>
        <td>android12-gsi(android-12.0.0_r28)</td>
        <td>27,308</td>
        <td>4,526,922</td>
        <td>650,983</td>
        <td>4</td>
        <td>2</td>
    </tr>
    <tr>
        <td>android-11</td>
        <td>25,866</td>
        <td>4,147,440</td>
        <td>502,111</td>
        <td>android12-gsi(android-11.0.0_r38)</td>
        <td>25,796</td>
        <td>4,131,630</td>
        <td>687,952</td>
        <td>178</td>
        <td>106</td>
    </tr>
    <tr>
        <td>android-10</td>
        <td>22,744</td>
        <td>3,711,094</td>
        <td>426,463</td>
        <td>android12-gsi(android-10.0.0_r41)</td>
        <td>22,558</td>
        <td>3,677,983</td>
        <td>650,983</td>
        <td>10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>android-9</td>
        <td>19,930</td>
        <td>3,186,526</td>
        <td>371,214</td>
        <td>android10-qpr2-release(android-9.0.0_r34)</td>
        <td>19,824</td>
        <td>3,173,299</td>
        <td>423,947</td>
        <td>43</td>
        <td>3</td>
    </tr>
    <tr>
        <td rowspan="2">IndustrialX</td>
        <td>S</td>
        <td>35,546</td>
        <td>5,866,790</td>
        <td>661,243</td>
        <td>android12-gsi(android-12.0.0_r10)</td>
        <td>27,161</td>
        <td>4,511,991</td>
        <td>648,567</td>
        <td>2</td>
        <td>2</td>
    </tr>
    <tr>
        <td>R</td>
        <td>31,181</td>
        <td>4,909,996</td>
        <td>491,418</td>
        <td>android12-gsi(android-11.0.0_r35)</td>
        <td>26,454</td>
        <td>4,152,622</td>
        <td>418,833</td>
        <td>14</td>
        <td>14</td>
    </tr>
</table>


## Table 2 The "older versions" specification(Review C Q1(2))

**Q: how are "older upstream versions" chosen?**

The commits in older upstream versions means these commits are not in the current latest merge points (i.e. android-12.1.0_r7 at android12-qpr3-s1-release for LineageOS-19.1 ) but in the whole commit history of upstream Android.

| Name        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| $Commits_U$ | All commits in the current latest merge points in current branch/version (i.e. android-12.1.0_r7 at android12-qpr3-s1-release for LineageOS-19.1 ) of upstream Android. |
| $Commits_D$ | All commits in the latest merge points in current branch/version (i.e. LineageOS-19.1) of downstream projects. |
| $Commits_O$ | All commits in the upstream commit history but not in $Commits_U$ |
| $U_e$       | The intersection of the commit set of the current entity and $Commits_U$ |
| $D_e$       | The intersection of the commit set of the current entity and $Commits_D$ |
| $O_e$       | The intersection of the commit set of the current entity and $Commits_O$ |



## Table 3 The combinations for enitity's ownership identification Parper P3 (Review C Q1(4) and Review A “Combination of Ue, De, and Oe”)

**Q: how does it deal with situations when (Ue!=0, De!=0, Oe!=0) or (Ue==0, De!=0, Oe!=0)?**

There are $2^3 = 8$ combinations for Ue, De, and Oe in sum，and here are the other 4 combinations we missed to present in paper.

| Ue                  | De                  | Oe                  | ownership               |
| ------------------- | ------------------- | ------------------- | ----------------------- |
| $\neq\emptyset$     | $=\emptyset$        | $=\emptyset$        | “actively native”       |
| $=\emptyset$        | $=\emptyset$        | $\neq\emptyset$     | "obsoletely native"     |
| $\neq\emptyset$     | $\neq\emptyset$     | $=\emptyset$        | "intrusively native"    |
| $=\emptyset$        | $\neq\emptyset$     | $=\emptyset$        | "extensive"             |
| $=\emptyset$        |   $=\emptyset$      |   $=\emptyset$      |   "IMPOSSIBLE"          |
| $=\emptyset$        |   $\neq\emptyset$   |   $\neq\emptyset$   |   "intrusive native"    |
|   $\neq\emptyset$== |   $\neq\emptyset$   |   $\neq\emptyset$   |   "intrusive native"    |
|   $\neq\emptyset$== |   $=\emptyset$      |   $\neq\emptyset$   |   "obsoletely native"   |



## Table 4  The formulaic definition of concepts (Review B)

**Q: . There is no formal definition that systematically describes the DepFCD model. It is better to clearly give out the definition of the dependency graph, updated graph, dependency facade, conflicts, etc.**

The formal definition of the dependency graph, updated graph, dependency facade, conflicts, etc.

| concept                    | description                                                  | definition                                                   |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| vertex set                 | The set of entities(vertexes) of dependency graph            | $V = \{e}\}$                                                |
| dependency set             | The set of edges(dependencies) of dependency graph           | $D = \{{d = e_i \to e_j}\}$                                  |
| dependency graph           | The initial dependency graph provided by ENRE                | $G = < V,  D>$                                               |
| entity's restriction level | The non-SDK restriction level of entities  imposed by Android | ${ e.restrict\_level\in\{’sdk’, 'unsupported’, 'max-target-x', 'blocked'\}}$ |
| entity's operation         | The operation downstream made to upstream entities           | ${e, e.operation\in\{'modify\ \ the\ \ modifier', 'modify\ \ the\ \ annotation', 'modify\ \ the\ \ parent\ class', etc\}}$ |
| entity's ownership         | The ownership of entities                                    | ${e, e.ownership\in\{'actively\ native', 'obsoletely\ native', 'intrusively\ native', 'extensive'\}}$ |
| updated graph              | The updated dependency graph, which included restriction level, operation, ownership | $G' = <V', D>, V' = \{{e, e.ownership\neq\emptyset, e.operation\neq\emptyset, e.restrict_level\neq\emptyset \}}$ |
| dependency facade          | The dependency facade which downstream coupling with upstream | $G_F = <V', D'> \\ D' = \{{d = e_i \to e_j, \\e_i.ownership == 'extensive'\  \&\& \ e_j.ownership.endwith('native') \cup \\e_j.ownership == 'extensive'\ \&\& \ e_i.ownership.endwith('native')}\\\}$ |
| conflicts                  | The entities which conflicts take place                      | ${e, e.conflict==CONFLICT\ BLOCK}$                           |



## Table 5 The description of metrics (Review B)

**Q: the definitions in section IV-A and the metrics Pact, Pins, Pext, Pobs, PE, and PD are all given without a description name and are hard to understand.**

The description name of the metrics Pact, Pins, Pext, Pobs, PE, and PD

| metrics   | description                                                  |
| --------- | ------------------------------------------------------------ |
| $P_{act}$ | the proportion of actively native entities in a downstream dependency graph $G^′_D.$ |
| $P_{ins}$ | the proportion of intrusively native entities in a downstream dependency graph $G^′_D.$ |
| $P_{ext}$ | the proportion of extensive entities in a downstream dependency graph $G^′_D.$ |
| $P_{obs}$ | the proportion of obsoletely native entities in a downstream dependency graph $G^′_D.$ |
| $PE$      | the proportion of entities $E_F$ in $G_F$ to all of the entities $E$ in $G^′_D.$ |
| $PD$      | the proportion of dependencies $D_F$ in $G_F$ to all of the dependencies $D$ in $G^′_D.$ |



## Table 6  The mapping between "Cases" and "Features" in Table VIII (Review C Q2, Q3)

**Q2:please clarify the mapping between the "Cases" column and the "Features" column in Table VIII?**

**Q3: please provide statistics (e.g., frequency counts) for the dependency facade in the "Features" column?**

The mapping between the "Cases" column and the "Features" column in Table VIII and the statistics (e.g., frequency counts) for the dependency facade in the "Features" column.

<table>
    <tr>
        <td>Conflict Location</td>
        <td>The Cases Regarding Downstream Modifications</td>
        <td>Features</td>
        <td>Frequency counts</td>
    </tr>
    <tr>
        <td rowspan="2">Method Block</td>
        <td>c</td>
        <td>⑩</td>
        <td>24</td>
    </tr>
    <tr>
        <td>a,b,d,e</td>
        <td>⑪</td>
        <td>108</td>
    </tr>
    <tr>
        <td rowspan="1">Class Field</td>
        <td>a,b</td>
        <td>⑧</td>
        <td>31</td>
    </tr>
    <tr>
        <td rowspan="3">Import</td>
        <td>a,b,c,d</td>
        <td>④</td>
        <td>31</td>
    </tr>
    <tr>
        <td>a,b</td>
        <td>⑤</td>
        <td>7</td>
	</tr>
    <tr>
        <td>a,b</td>
        <td>⑥</td>
        <td>4</td>
	</tr>
    <tr>
        <td rowspan="1">Parameters</td>
        <td>a,b</td>
        <td>⑨</td>
        <td>18</td>
    </tr>
    <tr>
        <td rowspan="1">Accessibility</td>
        <td>a,b,c</td>
        <td>①</td>
        <td>10</td>
    </tr>
    <tr>
        <td rowspan="3">Extensive method</td>
        <td>b</td>
        <td>⑤</td>
        <td>1</td>
    </tr>
    <tr>
        <td>a</td>
        <td>⑥</td>
        <td>3</td>
	</tr>
    <tr>
        <td>c</td>
        <td>⑮</td>
        <td>1</td>
	</tr>
    <tr>
        <td rowspan="2">Final</td>
        <td>a</td>
        <td>②</td>
        <td>2</td>
    </tr>
    <tr>
        <td>a</td>
        <td>⑧</td>
        <td>2</td>
    </tr>
    <tr>
        <td rowspan="1">Annotation</td>
        <td>a,b</td>
        <td>③</td>
        <td>2</td>
    </tr>
    <tr>
        <td rowspan="1">Inner-classes</td>
        <td>/</td>
        <td>⑦</td>
        <td>1</td>
    </tr>
</table>

### The "Others" in Table VIII:

1) “others” in Method blocks means the conflicts occur at the comment or javadoc;

2) “others” in Import means the conflicts take place due to importing built-in package or class;

3) “others” in Extensive method means downstream add extensive method in native file.

The 1. and 2. are not relative to dependency facade, 3. will lead to dependency edges from extensive to native entity, which is part of dependency facade.

### “49+16” in Table VIII:

- These conflicts（16） are due to git text matching errors and the conflict entity is not the same position as the place that actually changed；
- Meanwhile, there were some conflicts（49） in the Android itself during the upgrade process, which were repeated during the simulation, so these conflicts were classified as Upstream Update.



## Table 7  The comparison of percentage of dependencies from intrusively native to native (Review C Q1(3))

**C Q1(3):why is an "extensive" entity always required for detecting a dependency facade, say intrusive modifications?**

When an entity is identified as "intrusively native",  dependencies in it may originate from the upstream or created by the downstream. We calculated the percentage of dependencies between intrusively native and  native which upstream or downstream imposed.

| project            | the percentage of dependencies between intrusively native and native which upstream imposed | the percentage of dependencies between intrusively native and native which downstream imposed |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| AOSPA-Sapphire     | 98.55%                                                       | 1.45%                                                        |
| AOSPA-ruby-staging | 99.26%                                                       | 0.74%                                                        |
| AOSPA-quartz       | 99.15%                                                       | 0.85%                                                        |
| Calyxos-12         | 99.45%                                                       | 0.55%                                                        |
| Calyxos-11         | 99.35%                                                       | 0.65%                                                        |
| lineageOS-19.1     | 99.12%                                                       | 0.88%                                                        |
| lineageOS-18.1     | 98.81%                                                       | 1.19%                                                        |
| lineageOS-17.1     | 99.03%                                                       | 0.97%                                                        |
| lineageOS-16.0     | 99.01%                                                       | 0.99%                                                        |
| OmniROM-12.0       | 99.38%                                                       | 0.62%                                                        |
| OmniROM-11         | 99.03%                                                       | 0.97%                                                        |
| OmniROM-10         | 98.87%                                                       | 1.13%                                                        |
| OmniROM-9          | 98.99%                                                       | 1.01%                                                        |
| Industrial-S       | 97.55%                                                       | 2.45%                                                        |
| Industrial-R       | 97.80%                                                       | 2.20%                                                        |
| AVERAGE            | 98.38%                                                       | 1.62%                                                        |

According to table 7, we can see 98.38% dependencies between intrusively native and native are originated from the upstream, which should not be included in the dependency facade. And for the left 1.62% dependencies, we will study them in the next step.



## Table 8 The relation of two hotspots which RQ2 identified with conflicts we collected (Review C)

**Q: RQ2 also identifies two hotspots of intrusive modifications; it'd be more comprehensive if more statistics about all (or most) of the intrusive entities before giving the two hotspots. Also, may discuss more: what does it imply for an entity to be a hotspot? **

hotspot 1 : com.android.server.pm.PackageManagerService

hotspot 2 : android.provider.Settings

All versions of downstream projects have modified these 2 files. Thus, we count the conflict commits related to these 2 hotspots and find nearly 10% conflicts related to them.

<table>
   <tr>
      <td>project</td>
       <td>P(hotspot_1 / #CflCmt)</td>
       <td>P(hotspot_2 / #CflCmt)</td>
   </tr>
   <tr>
       <td>AOSPA-Sapphire</td>
       <td>7/37</td>
       <td>2/37</td>
   </tr>
   <tr>
       <td>AOSPA-Ruby</td>
       <td>4/47</td>
       <td>2/47</td>
   </tr>
   <tr>
       <td>AOSPA-Quartz</td>
       <td>2/52</td>
       <td>6/52</td>
   </tr>
   <tr>
       <td>CalyxOS-12</td>
       <td>0/2 </td>
       <td>0/2</td>
   </tr>
   <tr>
       <td>CalyxOS-11</td>
       <td>0/1 </td>
       <td>0/1</td>
   </tr>
   <tr>
       <td>LineageOS-19.1</td>
       <td>0/1 </td>
       <td>0/1</td>
   </tr>
   <tr>
       <td>LineageOS-18.1</td>
       <td>1/8 </td>
       <td>0/8</td>
   </tr>
   <tr>
       <td>LineageOS-17.1</td>
       <td>1/12 </td>
       <td>1/12</td>
   </tr>
   <tr>
       <td>LineageOS-16.0</td>
       <td>0/12 </td>
       <td>0/12</td>
   </tr>
   <tr>
       <td>OmniROM-12</td>
       <td>1/2</td>
       <td>0/2</td>
   </tr>
   <tr>
       <td>OmniROM-11</td>
       <td>7/106</td>
       <td>8/106</td>
   </tr>
   <tr>
      <td>OmniROM-10</td>
       <td>0/3</td>
       <td>0/3</td>
   </tr>
   <tr>
       <td>OmniROM-9</td>
       <td>0/3</td>
       <td>1/3</td>  
   </tr>
   <tr>
       <td>IndustrialX-S</td>
       <td>2/2</td>
       <td>1/2</td>  
   </tr>
   <tr>
      <td>IndustrialX-R</td>
       <td>10/14</td>
       <td>1/14</td>                                      
   </tr>
    <tr>
      <td>AVERAGE</td>
      <td colspan="2">9.45% </td>
   </tr>
   <tr>
      <td>SUMMARY</td>
      <td>35/302=11.6%</td>
      <td>22/302=7.3%</td>               
   </tr>
</table>


## Table 9 The top 2% conflict files in all conflicts we collected(Review C)

**Q: RQ2 also identifies two hotspots of intrusive modifications; it'd be more comprehensive if more statistics about all (or most) of the intrusive entities before giving the two hotspots. Also, may discuss more: what does it imply for an entity to be a hotspot? **

We counted the times each file conflicts and these 2 hotspots are in the top 2% conflict files. The hotspots indicates that the downstream versions commonly customize these classes and indeed incur merge conflicts.

| Files                                                        | Conflict times |
| ------------------------------------------------------------ | -------------- |
| services/core/java/com/android/server/ConnectivityService.java | 56             |
| services/core/java/com/android/server/am/ActivityManagerService.java | 55             |
| telephony/java/android/telephony/CarrierConfigManager.java   | 50             |
| services/core/java/com/android/server/audio/AudioService.java | 44             |
| services/core/java/com/android/server/wm/ActivityRecord.java | 40             |
| packages/SystemUI/src/com/android/systemui/statusbar/policy/MobileSignalController.java | 39             |
| services/core/java/com/android/server/BluetoothManagerService.java | 36             |
| ==services/core/java/com/android/server/pm/PackageManagerService.java== | 35             |
| services/core/java/com/android/server/wm/ActivityStack.java  | 35             |
| packages/SettingsLib/src/com/android/settingslib/bluetooth/CachedBluetoothDevice.java | 29             |
| services/core/java/com/android/server/am/ActiveServices.java | 27             |
| services/core/java/com/android/server/locksettings/LockSettingsService.java | 23             |
| wifi/java/android/net/wifi/WifiConfiguration.java            | 23             |
| services/core/java/com/android/server/audio/AudioDeviceBroker.java | 23             |
| core/java/android/bluetooth/BluetoothAdapter.java            | 23             |
| services/core/java/com/android/server/Watchdog.java          | 23             |
| ==core/java/android/provider/Settings.java==                 | 22             |
| services/core/java/com/android/server/wm/WindowManagerService.java | 21             |
| services/core/java/com/android/server/audio/BtHelper.java    | 21             |
| packages/SystemUI/src/com/android/systemui/statusbar/policy/WifiSignalController.java | 21             |



## Table 10 The manual checked results of our approach (Review A Q1)

**A Q1: The classification of native entities, especially the "obsoletely native entity".**

We conducted the manual check on the results of our approach for all projects we collected, and in all entities we selected randomly, 99.94% of them are true to life.

| project        | The number of entities manual checked | The number of wrong-identified entities manual checked | accuracy |
| -------------- | ------------------------------------- | ------------------------------------------------------ | -------- |
| AOSPA-Sapphire | 6747                                  | 3                                                      | 99.96%   |
| AOSPA-ruby     | 942                                   | 0                                                      | 100.00%  |
| AOSPA-quartz   | 720                                   | 0                                                      | 100.00%  |
| CalyxOS-12     | 229                                   | 4                                                      | 98.25%   |
| CalyxOS-11     | 440                                   | 0                                                      | 100.00%  |
| lineage-19.1   | 1029                                  | 0                                                      | 100.00%  |
| lineage-18.1   | 1269                                  | 0                                                      | 100.00%  |
| lineage-17.1   | 1322                                  | 0                                                      | 100.00%  |
| lineage-16.0   | 1079                                  | 0                                                      | 100.00%  |
| OmniROM-12     | 278                                   | 0                                                      | 100.00%  |
| OmniROM-11     | 1786                                  | 4                                                      | 99.78%   |
| OmniROM-10     | 1387                                  | 0                                                      | 100.00%  |
| OmniROM-9      | 1124                                  | 0                                                      | 100.00%  |
| SUMMARY        | 18352                                 | 11                                                     | 99.94%   |



 ## Table 11 The rebase and cherry-pick operations in downstream projects.(Review C Q4)

**Q: please comment on how conflicts caused by rebase, cherry-pick, etc. may be identified and related to the dependency facade?**

### In the open-source projects: 

- For rebase operation, according to [1], even though the rebasing branches rewrites the evolutionary history and the previous commits are missing after rebasing, it could be restored by identifying the force-pushed event that happened to the head branch of one pull request and then retrieving the missing commits. However, we do not find any force-pushed event in the downstream GitHub repos, which mean the downstream do not conduct "rebase".

- For cherry-pick operation, which could be restored by identifying the *"cherry picked from commit <commitid>”* in commit history[2], we collected all commits related to "cherry-pick" in the downstream commit history, which includes both upstream and downstream "cherry-pick". However, we only identified 8 cherry-picks combined with conflicts and they are all conducted by upstream.


| Project   | Commits number related to cherry-pick | Conflicts related to cherry-pick |
| --------- | ------------------------------------- | -------------------------------- |
| AOSPA     | 7484                                  | 8                                |
| CalyxOS   | 6773                                  | 8                                |
| LineageOS | 6749                                  | 8                                |
| OmniROM   | 6725                                  | 8                                |

<!--NOTE: These 8 commits are all the same.-->

### In the industrial projects:

Even though the "rebase" and "cherry-pick" commands are used during the development, "rebase" is hardly used and "cherry-pick" is used to synchronize a small number of problems in the downstream repo, the main problem is the conflicts caused by "merge".

> [1]T. Ji, L. Chen, X. Yi and X. Mao, "Understanding Merge Conflicts and Resolutions in Git Rebases," *2020 IEEE 31st International Symposium on Software Reliability Engineering (ISSRE)*, 2020, pp. 70-80, doi: 10.1109/ISSRE5003.2020.00016.
>
> [2]*Panuchart Bunyakiati and Chadarat Phipathananunth. 2017. Cherry-picking of code commits in long-running, multi-release software. In Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering (ESEC/FSE 2017). Association for Computing Machinery, New York, NY, USA, 994–998. https://doi.org/10.1145/3106237.3122818*
