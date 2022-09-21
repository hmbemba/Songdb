CREATE MIGRATION m1do4fbs7fmkd5mbfhzs4kqhwgzz54vkwfjqlzaaxg7btriundrtqa
    ONTO initial
{
  CREATE TYPE default::Song {
      CREATE REQUIRED PROPERTY artist -> std::str;
      CREATE PROPERTY bpm -> std::int32;
      CREATE PROPERTY key -> std::str;
      CREATE REQUIRED PROPERTY title -> std::str;
  };
};
