# /bin/bash
git pull
docker run --rm -v `pwd`:/work -w /work/frontend node:20-alpine sh -c "yarn install && yarn build"
docker-compose -f ./docker/docker-compose.yml up -d --build
