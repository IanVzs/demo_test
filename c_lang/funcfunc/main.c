#include <stdio.h>
#include <string.h>

int NUM_ADS = 5;
char *ADS[] = {
        "William: SBM GSON ilikes sports, TV, dining",
        "Matt: SWM NS likes art, movies, theater",
        "Luis: SLM ND likes books, theater, art",
        "Mike: DWM DS likes trucks, sporets and bieber",
        "Peter: SAM likes chess, working out and art",
};

int art_or_books_and_chess(char *s) {
        return (strstr(s, "movies") || !strstr(s, "chess") ) && strstr(s, "art");
}

int sports_no_bleber(char *s) {
        return strstr(s, "sports") && !strstr(s, "bieber");
}

void find_by_func(int (*func_match)(char *)) {
        // 如果传入的是个结构体，应该就能输出“名称”＋”结果”了吧
        int i;
        puts("Match results(by func):");
        puts("----------------------------");
        for (i = 0; i < NUM_ADS; i++) {
                if (func_match(ADS[i])) {
                        printf("%s\n", ADS[i]);
                }
        }
        puts("----------------------------");
}

void find() {

        int i;
        puts("Search results:");
        puts("----------------------------");

        for (i = 0; i < NUM_ADS; i++) {
                if (strstr(ADS[i], "sports") && !strstr(ADS[i], "bieber")) {
                        printf("%s\n", ADS[i]);
                        // break;
                }
        }
        puts("----------------------------");
}

int main() {
        find();
        find_by_func(sports_no_bleber);
        find_by_func(art_or_books_and_chess);
}

