#!/bin/zsh

VENV="virtualenv"

if [ -f "source_venv.sh" ]; then
    rm -rf make_venv.sh source_venv.sh $VENV
fi

touch make_venv.sh source_venv.sh
printf "#!/bin/zsh\n python -m venv $VENV\n" >> make_venv.sh
printf "#!/bin/zsh\nchmod u+x make_venv.sh\nsource make_venv.sh\n" >> source_venv.sh
if [ -f "source_venv.sh" ]; then
    chmod u+x source_venv.sh
    source ./source_venv.sh; source $VENV/bin/activate;
else printf "ERROR: no virtenv\n";
fi
