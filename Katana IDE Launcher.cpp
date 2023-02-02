#include <iostream>
#include <fstream>  
using namespace std;
int main()
{
	//ARGS Will add in next update
	cout << "Katana IDE Launcher v_0.1_alphaRelease\n";
	cout << "DON'T WHRITE BAD CODES\n\n";
	cout << "Output Will Printed into this Window : \n\n";
	ifstream ifile;
	ifile.open("usr_data\\launched.dat");
   if(ifile) {
      int retCode = system("IDE\\run.bat");
      cout << retCode;
   }else {
		ofstream outfile ("usr_data\\launched.dat");
		system("ci.bat");
		int retCode = system("IDE\\run.bat");
		outfile << "fisrt_time_launch = 0" << endl;
		outfile.close();
		cout << retCode;
   }

}