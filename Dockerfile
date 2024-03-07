FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# RUN apt-get update

RUN pip install --upgrade pip
RUN pip install matplotlib \
    && pip install pandas \
    && pip install seaborn \
    && pip install scikit-learn

RUN curl --location https://julialang-s3.julialang.org/bin/linux/x64/1.6/julia-1.6.7-linux-x86_64.tar.gz  > julia-1.6.7-linux-x86_64.tar.gz && \
    tar zxvf julia-1.6.7-linux-x86_64.tar.gz && \
    rm -rf julia-1.6.7-linux-x86_64.tar.gz && \
    cp -r julia-1.6.7 /usr/local/bin/ && \
    ln -s /usr/local/bin/julia-1.6.7/bin/julia /usr/local/bin/julia

RUN julia -e 'using Pkg; Pkg.add.(["OrdinaryDiffEq", "CSV", "DataFrames", "LinearAlgebra", "Roots", "JLD", "Statistics"])'


# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
