module default {

    type Song {
        required property title -> str{
            constraint exclusive;
        }
        required property artist -> str;
        property bpm -> int32;
        property key -> str;
        property songUrl -> str;

        }

}
