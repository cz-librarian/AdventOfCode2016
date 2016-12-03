#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
int main() {
	fstream input_file;
	char ch;
	signed int grid_size = 500;
	vector<string> instruction_list;
	vector< vector<int> > grid(grid_size, vector<int>(grid_size));
	string instruction;
	char facing = 'N';
	int distance = 0;
	int curr_x = 250;
	int curr_y = 250;
	input_file.open("input");
	
	// Read the instruction file
	while(input_file >> noskipws >> ch){
		if (ch == ' ' || ch == ',') {
			instruction_list.push_back(instruction);
			instruction = "";
		} else if('A' < ch ||  ch < 'Y' || 'a' < ch ||  ch < 'y' || '0' < ch || ch < '9') {
			instruction += ch;
		}
	}

	// Initialize the map
	for (int i = 0; i < grid_size; i++) {
		for (int j = 0; j < grid_size; j++) {
			grid[i][j] = 0;
		}
	}

	// Compute instructions
	for (auto i = instruction_list.begin(); i != instruction_list.end(); ++i) {
		if (size(*i) != 0) {
			//cout << curr_x << "," << curr_y << endl;
			instruction = (string)*i;
			distance = stoi(instruction.substr(1));
			if (instruction.at(0) == 'R') {
				if (facing == 'N') {
					facing = 'E';
					for (int i = 0; i < distance; i++) {
						curr_x += 1;
						if (grid[curr_x][curr_y] == 0){
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) +abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'E') {
					facing = 'S';
					for (int i = 0; i < distance; i++) {
						curr_y -= 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'S') {
					facing = 'W';
					for (int i = 0; i < distance; i++) {
						curr_x -= 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'W') {
					facing = 'N';
					for (int i = 0; i < distance; i++) {
						curr_y += 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}




			} else if (instruction.at(0) == 'L') {
				if (facing == 'N') {
					facing = 'W';
					for (int i = 0; i < distance; i++) {
						curr_x -= 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'E') {
					facing = 'N';
					for (int i = 0; i < distance; i++) {
						curr_y += 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'S') {
					facing = 'E';
					for (int i = 0; i < distance; i++) {
						curr_x += 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
				else if (facing == 'W') {
					facing = 'S';
					for (int i = 0; i < distance; i++) {
						curr_y -= 1;
						if (grid[curr_x][curr_y] == 0) {
							grid[curr_x][curr_y] += 1;
						}
						else {
							cout << "Visited " << curr_x << "," << curr_y << " second time." << endl;
							cout << "Position x" << curr_x - 250 << endl;
							cout << "Position y" << curr_y - 250 << endl;
							cout << "Distance from the beginning " << abs(curr_x - 250) + abs(curr_y - 250) << endl;
						}
					}
				}
			}
		}
	}
	
	system("pause");
	return EXIT_SUCCESS;
}