(om-start-udp-server 3003 "127.0.0.1" #'(lambda (msg) (let () 
                                                            (om::open-om-document (probe-file (second (car (process-osc-bundle (osc-decode msg) nil)))))
                                                            nil)))



(osc-send-message 9000 "127.0.0.1" (list "/send" "1"))


