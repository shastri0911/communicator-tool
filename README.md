#Readme to generate english sentence using a CHL input
######################################################

Pre-requisites:
--------------
1. pydelphin need to be installed in $HOME/
2. Ace parser 0.24 version or higher in $HOME/
3. Install the following packages
	libicu-dev flex

Set pydelphin and chl_to_dmrs path in ~/.bashrc:
-------------------------------
Copy below lines in end of ~/.bashrc 
export PYDELPHIN=$HOME/pydelphin
export DMRS=$HOME/chl_to_dmrs
export PATH=$DMRS/bin:$HOME/bin:$PATH


source ~/.bashrc

Compile:
-------
sh compile.sh

Run:
----
	bash run_communicator.sh <user.csv>
	       Ex: bash run_communicator.sh   user_csv/boy_can_eat_rice_with_the_spoon_user.csv 


#To generate only developer csv from user csv:
#############################################
	bash convert_user_to_dev_csv.sh  <user.csv> <dev.csv>
		Ex: bash convert_user_to_dev_csv.sh boy_can_eat_rice_with_the_spoon_user.csv dev.csv

#To run only devloper csv:
#########################	
	bash run.sh <dev.csv>
		Ex: bash run.sh sleep.csv


#If sentence is not generated, to generate sentence by changing dmrs manually :
#############################################################################
1. If the sentence is not generated then, modify vi output/<file_name>_dev.csv_new_dmrs.txt manually.
2. Now run,
	bash run_mod_dmrs.sh <dev.csv>
		Ex: bash run_mod_dmrs.sh boy_can_eat_rice_with_the_spoon_dev.csv
		(Note: If above modification is correctly done, sentence is generated)

#To run complex sentences using header file:
############################################
	bash convert_user_to_dev_csv_using_header_file.sh <header-file>
		Ex: bash convert_user_to_dev_csv_using_header_file.sh header_files/rAma_vixyAlaya_jA_rahA_hE_kyoM_ki_mEMne_usase_kahA.txt
		(Note: Complex sentences need to be splitted into small sentences and 
			these small sentences user csv's should be present in same folder where header file is present.
		)
