use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader, Seek},
};

mod prob1;
mod prob2;

fn main() -> Result<(), Box<dyn Error>> {
    let file = File::open("input.txt")?;
    let mut reader = BufReader::new(file);
    let mut lines = (&mut reader).lines();

    let r1 = prob1::solve(&mut lines)?;
    println!("{}", r1);

    reader.rewind()?;
    lines = (&mut reader).lines();

    let r2 = prob2::solve(&mut lines)?;
    println!("{}", r2);

    Ok(())
}
