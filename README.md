# Project Trajectories and Feedback Data

This repository contains detailed trajectories, progress, and feedback data collected from a study. The data includes trajectories in both `.bag` and text format, end-effector positions, progress metrics, scalar feedback, and the positions of objects used in the study.

## File Descriptions

- **.bag Files**: These files contain the trajectories in ROS bagfile format, specifically in `JointState()` message form.
- **pose.txt**: Records the end-effector (eef) positions.
- **progress.txt**: Contains progress data.
- **scalar.txt**: Holds scalar feedback from the study.
- **step.txt**: Records the points at which progress and scalar feedback were collected.
- **obj_pose.txt**: Details all the positions of the objects used in the study.
- **jar_picked_for_each_participant.txt**: Logs which jar was picked by each participant, in order.

## Code Files

- **read_txt_data.ipynb**: An example Jupyter notebook that demonstrates how to read all the `.txt` files mentioned above.
- **Read_trajectories_from_bags.py**: A Python script for reading all `.bag` files, extracting trajectory data.

## Usage

To use the data and scripts provided in this repository, you should have a Python environment capable of running Jupyter notebooks and a ROS environment for handling `.bag` files.

### Reading Text Data

1. Ensure you have Jupyter Notebook installed.
2. Navigate to the directory containing `read_txt_data.ipynb`.
3. Open the notebook by running `jupyter notebook read_txt_data.ipynb` in your terminal.
4. Follow the instructions within the notebook to read and analyze the text data.

### Reading .bag Files

1. Ensure your system has ROS installed and configured.
2. Place the `Read_trajectories_from_bags.py` script in your workspace.
3. Run the script using `python Read_trajectories_from_bags.py`.
4. The script will output the trajectory data stored in the `.bag` files.

## Contributing

We welcome contributions to improve the scripts or expand the dataset. Please feel free to open an issue or submit a pull request.

## License

MIT License
