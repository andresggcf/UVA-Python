#include <iostream>
#include <stdlib.h>
#include <string>
#include <list>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;


vector<string> split_str (string str){
    stringstream ss( str );
    vector<string> resultado;

    while( ss.good() )
    {
        string substr;
        getline( ss, substr, ',' );
        resultado.push_back( substr );
    }
    return resultado;
}

int main (){
    int cant_dep, i,j;
    vector < vector <string> > blackb;
    string dep, persona;
    vector<string> pers;
    
    cin >> cant_dep; //cantidad de departamentos
    cin.ignore();
    if (cant_dep >= 2 && cant_dep <= 12){
        for(i=0; i < cant_dep; i++){
            getline(cin, dep); //nombre del departamento
            //cout << "dep " << dep <<" "<< i<<endl; 
            while (1){ //ciclo infinito porque no se sabe cuantos empleados hay
                getline(cin, persona);
                pers = split_str(persona);
                if(blackb.size() == 0){
                    blackb.push_back(pers); //inserta persona al inicio
                }
                else{
                    
                }
                cout <<blackb[0][2]<<endl;
                cout << pers[2];
                
                //for (int i=0; i< pers.size(); i++)
                  //  cout << pers.at(i)<<" ";
                //cout << "Persona "<<split_str(persona);<<endl;
                break;
            }
        }
    }
}