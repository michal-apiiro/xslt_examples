package monitor

import (
	"net/http"
	"log"
)

type MonitorController struct {
	Address string
	Monitor *WorkerMonitor
	mux *http.ServeMux
}

func NewMonitorController(address string, monitor *WorkerMonitor) *MonitorController {
	controller := &MonitorController{
		Address: address,
		Monitor: monitor,
		mux:     http.NewServeMux(),
	}
	controller.AddRoutes()
	return controller
}

func (c *MonitorController) AddRoutes() {
	c.mux.HandleFunc("/debug", func(writer http.ResponseWriter, request *http.Request) {
		log.Infof("hey debug")
	})

	c.mux.HandleFunc("/debug-disable", func(writer http.ResponseWriter, request *http.Request) {
		log.Infof("hey debug2")
	})

	c.mux.HandleFunc("/restart", func(writer http.ResponseWriter, request *http.Request) {
		log.Infof("hey restart")
		// Include restart logic here if needed
	})
}
