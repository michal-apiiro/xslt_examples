package packagee

import (
	"net/http"
	"github.com/gorilla/mux"
	"github.com/sirupsen/logrus"
)


func (this *ControlServer) Initialize() (err error) {
	this.router = mux.NewRouter()
	this.router.HandleFunc("/", this.HandleIndex).Methods("GET")
	this.router.HandleFunc("/api/status", this.HandleStatus).Headers("Content-Type", "application/json").Methods("GET")
}

func (this *ControlServer) HandleIndex(w http.ResponseWriter, r *http.Request) {
	status := this.fetchStatus()
}

func (this *ControlServer) HandleStatus(w http.ResponseWriter, r *http.Request) {
	status := this.fetchStatus()
	}


