CREATE MIGRATION m12wrmyu5a2me3ws4xa6bzhgvmvv2bhcilxb4g4vcz6vcfxubzo6mq
    ONTO m1st6hgqtwprbnn7gi32z6j76lf27iuei6q22knnah4ytw4cv55wqa
{
  ALTER TYPE default::Song {
      ALTER PROPERTY title {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
