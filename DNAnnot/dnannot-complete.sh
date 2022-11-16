
    Welcome to Annotator version: 1.0.0 ! Created on November 2019
    @author: Florian Charriat (INRAE), Sebastien Ravel (CIRAD), ,
    @email: florian.charriat@inrae.fr; sebastien.ravel@cirad.fr

    Please cite our github https://DNANNOT-pipeline.readthedocs.io/en/latest/
    Licencied under CeCill-C (http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html)
    and GPLv3 Intellectual property belongs to INRAE, CIRAD and authors.
    Documentation avail at: https://DNANNOT-pipeline.readthedocs.io/en/latest/
    
    ** ENABLE TO GET LAST VERSION, check internet connection
HTTP Error 404: Not Found

_dnannot_completion() {
    local IFS=$'\n'
    local response

    response=$(env COMP_WORDS="${COMP_WORDS[*]}" COMP_CWORD=$COMP_CWORD _DNANNOT_COMPLETE=bash_complete $1)

    for completion in $response; do
        IFS=',' read type value <<< "$completion"

        if [[ $type == 'dir' ]]; then
            COMPREPLY=()
            compopt -o dirnames
        elif [[ $type == 'file' ]]; then
            COMPREPLY=()
            compopt -o default
        elif [[ $type == 'plain' ]]; then
            COMPREPLY+=($value)
        fi
    done

    return 0
}

_dnannot_completion_setup() {
    complete -o nosort -F _dnannot_completion dnannot
}

_dnannot_completion_setup;

