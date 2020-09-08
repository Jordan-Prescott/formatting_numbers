This script is for my work colleague who when entering numbers into our hosted solution would like a script to format the numbers correctly.

How the numbers are sent to him:
312.321.7100 – 7109;
312.321.7111;
312.321.7114 – 7115;
312.321.7117 – 7155;
312.321.7157 – 7158;
309.309.7111 - 7120;

How the numbers need to be for the system to allow him to build:
3123217100 - 3123217109
3123217111
3123217114 - 3123217115
3123217117 - 3123217155
3123217157 - 3123217158
3093097111 - 3093097120

Format rules
1. The first 6 of the range needs to be added and the same as the ones without the begging
    - You can see in the exmaple 309309 at the bottom is different so the script has to notice this
2. The punctuaction needs to be removed - . ;