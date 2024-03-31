CURRENT=${PWD}



cd ${CURRENT}/monitoring && kubectl apply -n istio-system  -f . 
