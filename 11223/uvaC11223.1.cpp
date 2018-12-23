#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <fstream>
#include <vector>


using namespace std;

int main(){

	string vv[53] = {".-","-...","-.-.","-..",".","..-.",
	"--.","....","..",".---" ,"-.-", ".-..","--",
	"-.","---",".--.","--.-",".-.","...","-",
	"..-","...-", ".--","-..-", "-.--", "--..",
	"-----",".----","..---","...--","....-",".....",
	"-....","--...","---..","----.",".-.-.-","--..--",
	"..--..",".----.","-.-.--","-..-.","-.--.","-.--.-",
	".-...", "---...","-.-.-.","-...-",".-.-.","-....-",
	"..--.-",".-..-.",".--.-."}; 
	vector<string> v1(vv,vv + sizeof(vv)/sizeof(string));

	char vv2[53] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'
	, 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', '\'', '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '\"', '@' };
	vector<char> v2(vv2,vv2 + sizeof(vv2)/sizeof(char));

	int c, i, j , t;
	string  x;
	ifstream infile;
	infile.open("11223.in");
	
	if (infile.fail()){
		cerr<<"Error al abrir el archivo"<<endl;
		exit(1);
	}
	infile >> t;
	if (t <= 10){
		string text;
		getline(infile, text);
		for(int m = 0; m < t; m++){
			x = "";
			getline(infile, text);
			text += ' '; // agrega un espacio despues del string ...- --> ...-' '
			cout << "Message #"<< m + 1 << endl;
			if (text.size() <= 2000){
				//cout << "text.size <= 2000" << endl;
				for(i = 0; i < text.size(); i++){
				//	cout << "primer for: " << endl;
				//	cout << "text: " << text <<endl;
					if(text[i] != ' '){ //si en el string hay algo diferente a espacio
						x = x + text[i];
				//		cout << "x : " << x  << "text " << text[i]<< endl;
					}
					else{ 
						for(j = 0; j < 53 ; j++){
							if(x == v1[j]){
								cout << v2[j];
								x = "";
							}
						}
						if(text[i-1] == ' '){ //si hay dos espacios seguidos
							cout << " ";
						}
					}
					if (i == (text.size()-1) && m < t-1)
						cout << endl << endl;
					
					//cout<<"i: "<< i << text.size() <<endl;
					
				}
			}
		}
	}
	return 0;
}
