//Danny Radosevich
//A simple server to handle http requests
// Web App Development

package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	fmt.Println("starting up....")
	var err error

	//db, err = pgxpool.Connect(context.Background(), os.Getenv("DB_CONN")) //connect to DB

	//fs := http.FileServer(http.Dir("./static"))
	//http.Handle("/", fs)
	http.HandleFunc("/", landingFunc)
	//http.HandleFunc("/login", userLogin)
	http.HandleFunc("/addfile", addFile)
	http.HandleFunc("/showfiles", myLS)
	err = http.ListenAndServe(":8080", nil) // setting listening port
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}

}
func myLS(w http.ResponseWriter, r *http.Request) {
	//stolen from: https://stackoverflow.com/questions/14668850/list-directory-in-go
	files, err := ioutil.ReadDir("./")
	if err != nil {
		log.Fatal(err)
	}

	for _, f := range files {
		fmt.Println(f.Name())
	}
}

func landingFunc(w http.ResponseWriter, r *http.Request) {
	//fmt.Println("Meth-od:", r.Method) //get request method
	//fmt.Println("serving up the form hopefully maybe")
	if r.Method == "GET" {
		//go exec to find where the gtpl file is
		//cmd := exec.Command("find . -n \"land.gtpl\"")
		//stdout, err := cmd.Output()
		//fmt.Println("found the file at ", stdout)
		t, err := template.ParseFiles(string("./land.gtpl"))
		if err != nil {
			//myLS()
			//FilePathWalkDir("./")
			log.Fatalln(err)
		}
		t.Execute(w, nil)
	}
}
func addFile(w http.ResponseWriter, r *http.Request) {
	//fmt.Println(r)
	if r.Method == "POST" {
		my_body := r.Body
		fmt.Println(my_body)

	}

}
