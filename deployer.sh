CURRENT=${PWD}

cd ${CURRENT}/ && kubectl apply -f  namespace.yml
cd ${CURRENT}/ && kubectl apply -f  loki-dns.yml
cd ${CURRENT}/api-gateway && kubectl apply -f .
cd ${CURRENT}/math-add-subtract && kubectl apply -f .
cd ${CURRENT}/math-division-multiplication && kubectl apply -f .
cd ${CURRENT}/services-discovery-eureka && kubectl apply -f .
