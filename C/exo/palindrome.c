#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    int num = 0;
    scanf("%d\n", &num);
    
    for (int i = 0; i < num; i++) {
        char ligne[100];
        scanf("%[^\n]%*c", ligne);
        
        int debut = 0;
        int fin = strlen(ligne) - 1;
        int verif = 0;
        
        while (debut < fin) {
            // Ignorer les caractères non alphabétiques
            while (!isalpha(ligne[debut]) && debut < fin)
                debut++;
            
            while (!isalpha(ligne[fin]) && debut < fin)
                fin--;
            
            if (tolower(ligne[debut]) != tolower(ligne[fin])) {
                verif = 1;
                break;
            }
            
            debut++;
            fin--;
        }
        
        if (verif == 0) {
            printf("%s\n", ligne);
        }
    }
    
    return 0;
}

