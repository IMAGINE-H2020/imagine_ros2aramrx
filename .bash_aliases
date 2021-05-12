alias qt='cd ~/QtCreator/latest/bin && ./qtcreator'

##### ROS, workspace #####
alias siros='source ~/imagine_ws/devel/setup.bash'
alias sros='if [ -z "$SROS_HAS_RUN" ] ; then source ~/imagine_ws/devel/setup.bash && source ~/cvbridge_build_ws/install/setup.bash --extend && export SROS_HAS_RUN=1; fi'


##### ADES #####
alias ades='sros && rosrun uibk_libades_ros adesdb --home ~/repo/ades_database_kitgripper'
alias ades2='sros && roslaunch ros2armarx launch_ades.launch'
alias listades='sros && rosservice call /ades2db/list_ades'


#### ARMARX #####
alias as='armarx start'
alias ag='armarx gui'
alias am='armarx memory start'
alias astart='as && am && ag'
alias ap='armarx stop'
alias astop='armarx memory stop && ap'
alias ak='armarx killAll'
alias aki='armarx killIce'
alias kg='pkill -9 ArmarXGuiRun'
alias ra='armarx reset'
##### make
alias mi='MAKEFLAGS="-j12" armarx-dev build Imagine -j12'


##### training screw localizer KIT-ArmarX #####
alias tf2='ana && conda activate tf2'
alias tf='ana && conda activate tf'
alias trainscrew='/common/homes/staff/imagine-user/repo/armarx/Imagine/etc/scripts/convNet.py.in --pos_input_dir=/common/homes/staff/imagine-user/repo/kit_gripper_screw_database/SortedImg_KIT/Screw --neg_input_dir=/common/homes/staff/imagine-user/repo/kit_gripper_screw_database/SortedImg_KIT/NoScrew --is_train --old_model_dir /common/homes/staff/imagine-user/repo/armarx/Imagine/data/Imagine/ScrewLocalizer'


##### Git aliases by Rainer Kartmann - let me now if you don't like them
alias gs="git status"
alias gl="git log --all --oneline --decorate --graph"
alias gd="git diff"
alias gg="git gui"
alias gf="git fetch"
alias gfm="git fetch origin master:master"
alias grp="git remote prune origin"
alias gk="gitk --all"

##### azure kinect
alias kinect="source ~/Downloads/SetupAzureKinect.sh && azure_kinect_activate"

##### singularity
alias sing='singularity shell --nv ~/singularity/iis-robot.sif'


##### conda virtual env
alias iv='source ~/ugoe_env/bin/activate && sros'
alias iv2='ana && source $HOME/cvbridge_build_ws/devel/setup.bash --extend && conda activate imagine-venv2'


##### pylon
alias pylon='sros && roslaunch pylon_camera pylon_camera_node.launch'
alias pylon1='ROS_NAMESPACE=/pylon_camera_node rosrun image_proc image_proc'
##### nerian
alias nerian='roslaunch nerian_stereo nerian_stereo.launch'
alias nerian1='cd ~/repo/nerian-vision-software-8_3_0-src/bin && ./nvcom'


##### perception nodes
alias screw='source ~/ugoe_env/bin/activate && sros && rosrun ugoe_screw_detection_ros candidate_generator.py'
alias gap='source ~/ugoe_env/bin/activate && sros && rosrun ugoe_gap_detection_ros gap_detector.py'

#### Setup
alias setup='sros && roslaunch ros2armarx kit_setup.launch'
alias krviz='sros && roslaunch ros2armarx kit_rviz.launch'



