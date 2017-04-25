from rattle import Run

RUN = Run(config)

include: "includes/qc/Snakefile"
include: "includes/itd-flt3/Snakefile"

rule all:
    input:
        fqs=[RUN.output("{sample}/{sample}-{pair}.fq.gz", fmt=True,
                        sample=unit.sample, pair=pair)
             for unit in RUN.unit_names for pair in ("R1", "R2")],
        flt3_sc_jsons=expand(RUN.output("{sample}/{sample}.flt3-sc.json"), sample=RUN.samples),
        flt3_sc_plots=expand(RUN.output("{sample}/{sample}.flt3-sc.png"), sample=RUN.samples),

