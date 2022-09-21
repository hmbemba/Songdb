CREATE MIGRATION m1st6hgqtwprbnn7gi32z6j76lf27iuei6q22knnah4ytw4cv55wqa
    ONTO m1do4fbs7fmkd5mbfhzs4kqhwgzz54vkwfjqlzaaxg7btriundrtqa
{
  ALTER TYPE default::Song {
      CREATE PROPERTY songUrl -> std::str;
  };
};
