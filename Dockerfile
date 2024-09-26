FROM mongodb/mongodb-community-server:7.0.4-ubi9

ENV MONGO_INITDB_ROOT_USERNAME=mongodb
ENV MONGO_INITDB_ROOT_PASSWORD=mongodb


EXPOSE 27017