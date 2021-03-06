#!/usr/bin/env python

import json
import sys

import click
from crimson import fastqc


def parse_fastqc_stats(fastqc_dir):
    raw = fastqc.parse(fastqc_dir)
    stats = {
        "pct_gc": raw["Basic Statistics"]["contents"]["%GC"],
        "num_seq": raw["Basic Statistics"]["contents"]["Total Sequences"],
    }
    return stats


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("raw_fastqc_r1_dir",
                type=click.Path(exists=True, file_okay=False))
@click.argument("raw_fastqc_r2_dir",
                type=click.Path(exists=True, file_okay=False))
@click.argument("proc_fastqc_r1_dir",
                type=click.Path(exists=True, file_okay=False))
@click.argument("proc_fastqc_r2_dir",
                type=click.Path(exists=True, file_okay=False))
@click.option("--name", type=str)
def main(raw_fastqc_r1_dir, raw_fastqc_r2_dir,
         proc_fastqc_r1_dir, proc_fastqc_r2_dir, name):
    stats = {
        "name": name,
        "raw": {
            "R1": parse_fastqc_stats(raw_fastqc_r1_dir),
            "R2": parse_fastqc_stats(raw_fastqc_r2_dir),
        },
        "proc": {
            "R1": parse_fastqc_stats(proc_fastqc_r1_dir),
            "R2": parse_fastqc_stats(proc_fastqc_r2_dir),
        },
    }
    json.dump(stats, sys.stdout, separators=(",", ":"))


if __name__ == "__main__":
    main()
